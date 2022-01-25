from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMIN = env.str("ADMIN")
RECEIVER = env.str("RECEIVER")
IP = env.str("ip")

