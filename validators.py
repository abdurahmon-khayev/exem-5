def validation_user_on_create(username, password):
    assert username, 'Username is required'
    assert password, 'Password is required'
