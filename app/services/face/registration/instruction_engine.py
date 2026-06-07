class InstructionEngine:

    def get_instruction(self, checks):

        priority = [

            "face_size",

            "face_position",

            "face_angle",

            "brightness",

            "blur"

        ]

        for checker_name in priority:

            for check in checks:

                if (
                    check["name"] == checker_name
                    and not check["passed"]
                ):

                    return check["message"]

        return "READY FOR REGISTRATION"