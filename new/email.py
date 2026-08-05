def replace_domain(email, old_domain, new_domain): 

    if '@' + old_domain in email : # checks --> if "@olddomain.com" present in email
        index = email.index("@" + old_domain)  # which position does "@old.com" has
        print(index)    # 4th position

        # adds all user_name right before the '@' sign, the add @ and then add the new_domain (replace)
        new_emil = email[:index] + "@" + new_domain   
        return new_emil
    return email


result = replace_domain("user@olddomain.com", "olddomain.com", "newdomain.com")

print(result)