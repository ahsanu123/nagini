from nagini.https.emiten_codes import EmitenCode


def test_get_all_emiten_code():
    allCodes = EmitenCode.getAllCodes()
    print(allCodes)
