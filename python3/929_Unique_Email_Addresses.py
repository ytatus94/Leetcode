class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = []
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.','')
            unique_emails.append(local + '@' + domain)
        return len(set(unique_emails))
