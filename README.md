# mc-plugin-str-creator

A Python CLI tool to scaffold a basic Minecraft plugin folder structure with:

- `pom.xml`
- `Main.java`
- `plugin.yml`
- `config.yml`
- `messages.yml`

Import it in:

```python
from mc_plugin_strcreator.generator import create_mc_pl_src

# Example usage
create_mc_pl_src(plugin_name="Testing", author_name="NotGamerPratham")
```
