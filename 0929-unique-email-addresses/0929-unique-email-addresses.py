
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            local, domain = email.split("@")

            local = local.split("+")[0]
            local = local.replace(".", "")

            new_email = local + "@" + domain

            unique.add(new_email)

        return len(unique)
