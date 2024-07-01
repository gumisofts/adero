from django.apps import AppConfig

# import subprocess


# p = subprocess.Popen(
#     "npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css",
#     shell=True,
#     stdout=subprocess.PIPE,
#     stderr=subprocess.STDOUT,
# )
# for line in p.stdout.readlines():
#     print(line)
# retval = p.wait()


class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"
