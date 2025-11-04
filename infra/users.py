from aws_cdk import aws_iam as iam, aws_secretsmanager as secrets_manager
from constructs import Construct


class LibraryUser(Construct):
    """
    This is a construct that wraps up an IAM User with the policies required to secure it
    """
    def __init__(self, scope: Construct, id: str, username: str):
        super().__init__(scope, id)

        # Generate a secure password in Secrets Manager
        password_secret = secrets_manager.Secret(
            self, "PasswordSecret",
            generate_secret_string=secrets_manager.SecretStringGenerator(
                exclude_punctuation=True,
                include_space=False,
                password_length=16
            )
        )

        # Create IAM user with console access
        self.user = iam.User(
            self, "User",
            password=password_secret.secret_value,
            password_reset_required=True,
            user_name=username
        )

        # allow the user to change their password
        self.user.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "IAMUserChangePassword"
            )
        )

        # require users to have multi-factor authentication
        mfa_enforce_policy = iam.Policy(
            self, "MfaEnforcePolicy",
            statements=[
                iam.PolicyStatement(
                    effect=iam.Effect.DENY,
                    actions=["*"],
                    resources=["*"],
                    conditions={
                        "BoolIfExists": {"aws:MultiFactorAuthPresent": "false"}
                    }
                )
            ]
        )
        mfa_enforce_policy.attach_to_user(self.user)
