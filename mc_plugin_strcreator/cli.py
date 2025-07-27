# mc_plugin_strcreator/cli.py

from .generator import create_mc_pl_src

def main():
    plugin_name = input("Enter the plugin name: ")
    author_name = input("Enter the author name: ")
    create_mc_pl_src(plugin_name, author_name)
    print(f"\n✅ Plugin structure for '{plugin_name}' created successfully!")

if __name__ == "__main__":
    main()
