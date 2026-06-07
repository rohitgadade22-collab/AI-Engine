class RegistrationScore:

    def calculate(self, checks):

        if not checks:

            return {
                "score": 0,
                "ready": False
            }

        total = len(checks)

        passed = sum(
            1 for check in checks
            if check["passed"]
        )

        score = int((passed / total) * 100)

        return {

            "score": score,

            "ready": score >= 80

        }