from collections import namedtuple

Category = namedtuple('Category', ('name', 'symbol', 'codes'))


def categories_helper():
    categories = [
        Category('Подорожі', '🚆', [4011, 4111, 4112, 4131, 4304, 4411, 4415, 4418, 4457, 4468, 4511, 4582, 4722, 4784, 4789, 5962, 6513, 7011, 7032, 7033, 7512, 7513, 7519] + list(range(3000, 4000))),
        Category('Краса та медицина', '🏥', [4119, 5047, 5122, 5292, 5295, 5912, 5975, 5976, 5977, 7230, 7297, 7298, 8011, 8021, 8031, 8049, 8050, 8062, 8071, 8099] + list(range(8041, 8044))),
        Category('Розваги та спорт', '🎾', [5733, 5735, 5941, 7221, 7333, 7395, 7929, 7932, 7933, 7941, 7991, 7995, 8664] + list(range(5970, 5974)) + list(range(5945, 5948)) + list(range(5815, 5819)) + list(range(7911, 7923)) + list(range(7991, 7995)) + list(range(7996, 8000))),
        Category('Кафе та ресторани', '🍴', list(range(5811, 5815))),
        Category('Продукти й супермаркети', '🏪', [5297, 5298, 5300, 5311, 5331, 5399, 5411, 5412, 5422, 5441, 5451, 5462, 5499, 5715, 5921]),
        Category('Кіно', '🎞', [7829, 7832, 7841]),
        Category('Авто та АЗС', '⛽', [5172, 5511, 5541, 5542, 5983, 7511, 7523, 7531, 7534, 7535, 7538, 7542, 7549] + list(range(5531, 5534))),
        Category('Одяг і взуття', '👖', [5131, 5137, 5139, 5611, 5621, 5631, 5641, 5651, 5655, 5661, 5681, 5691, 5697, 5698, 5699, 5931, 5948, 5949, 7251, 7296]),
        Category('Таксі', '🚕', [4121]),
        Category('Тварини', '🐈', [742, 5995]),
        Category('Книги', '📚', [2741, 5111, 5192, 5942, 5994]),
        Category('Квіти', '💐', [5992, 5193]),
        Category('Поповнення мобільного', '📞', [4814]),
        Category('Грошові перекази', '💸', [4829]),
        Category('Комунальні послуги', '🚰', [4900]),
        Category('Інше', '❓', [])
    ]

    result = []
    for category in categories:
        result.append({"category": category.name, "codes": category.codes})

    return result