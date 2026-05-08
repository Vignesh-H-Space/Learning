def check_password(password):
    if len(password) < 8:
        return "Weak"

    has_digit = False

    for ch in password:
        if ch.isdigit():
            has_digit = True

    if has_digit:
        return "Strong"
    else:
        return "Medium"


pwd = "python123"

print(check_password(pwd))