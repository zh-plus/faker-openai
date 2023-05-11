from openfaker import Faker
from lingua import LanguageDetectorBuilder

faker = Faker()


def test_name():
    assert len(faker.name(10)) == 10
    assert len(faker.name(5)) == 5
    assert len(faker.name(20)) == 20


def test_address():
    assert len(faker.address(10)) == 10
    assert len(faker.address(5)) == 5
    assert len(faker.address(20)) == 20


def test_color():
    print(faker.color(10))


def test_locale():
    detector = LanguageDetectorBuilder.from_all_languages().with_preloaded_language_models().build()

    cn_name = faker.name(locale='CN')
    assert detector.detect_language_of(cn_name).name.lower() == 'chinese'

    jp_name = faker.name(locale='RU')
    assert detector.detect_language_of(jp_name).name.lower() == 'russian'
