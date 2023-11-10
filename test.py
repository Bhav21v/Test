import os
import yaml

with open('input.yaml','r') as file:
  data = yaml.safe_load(file)

with open(os.environ['GITHUB_ENV'], 'a') as github_env_file:
    for key, value in data.items():
      x = f"{key}"
      for key, value in value.items():
          y = f"{x}_{key}"
          os.environ[y] = str(value)
          github_env_file.write(f"{y}={os.environ[y]}\n")
