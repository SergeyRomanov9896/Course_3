from configparser import ConfigParser
from pathlib import Path


def load_db_config(
    dbname: str,
    section: str = "Database",
) -> dict[str, str]:
    """Читает настройки подключения из INI и добавляет имя базы данных."""
    config_path = Path(__file__).resolve().parents[2] / "database.ini"

    parser = ConfigParser(interpolation=None)

    with config_path.open(encoding="utf-8") as config_file:
        parser.read_file(config_file)

    if not parser.has_section(section):
        raise ValueError(
            f"В файле {config_path.name} отсутствует секция [{section}]"
        )

    params = dict(parser[section])

    required_keys = ("host", "user", "password")
    missing_keys = [
        key
        for key in required_keys
        if not params.get(key, "").strip()
    ]

    if missing_keys:
        raise ValueError(
            "Не заполнены параметры подключения: "
            + ", ".join(missing_keys)
        )

    params["dbname"] = dbname

    return params
