import supabase

"""
Convert this flow into a test
client = supabase.Client("<insert link>", "<password>")
client.auth.sign_up({"email": "anemail@gmail.com", "password": "apassword"})
"""


def test_dummy() -> None:
    # Test auth component
    assert True


def test_client_initialziation() -> None:
    _ = supabase.Client("http://testwebsite.com", "atestapi")
