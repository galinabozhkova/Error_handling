class CustomError (Exception):
    pass

class NameTooShortError(CustomError):
    pass

class MustContainAtSymbolError(CustomError):
    pass

class InvalidDomainError(CustomError):
    pass

email = input()

while email!="End":
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name = email.split("@")[0]
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = email.split(".")[-1]
    if domain not in ["com", "bg", "org", "net"]:
        raise InvalidDomainError ("Domain must be one of the following: .com, .bg, .org, .net")

    email = input()