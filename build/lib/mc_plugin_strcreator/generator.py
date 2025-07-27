# mc_plugin_strcreator/generator.py

import os

def create_mc_pl_src(plugin_name: str, author_name: str):
    """
    Creates a Minecraft plugin structure with a pom.xml file and a main class.
    """
    author_dir = author_name.lower()
    java_path = f"src/main/java/com/{author_dir}/{plugin_name.lower()}"
    os.makedirs(java_path, exist_ok=True)
    os.makedirs("src/main/resources", exist_ok=True)

    # Create pom.xml
    with open("pom.xml", "w") as f:
        f.write(f"""<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.{author_dir}</groupId>
    <artifactId>{plugin_name.lower()}</artifactId>
    <version>1.0-SNAPSHOT</version>
    <name>{plugin_name}</name>
</project>""")

    # Create Main.java
    with open(f"{java_path}/Main.java", "w") as f:
        f.write(f"""package com.{author_dir}.{plugin_name.lower()};

import org.bukkit.plugin.java.JavaPlugin;

public class Main extends JavaPlugin {{
    @Override
    public void onEnable() {{
        getLogger().info("{plugin_name} has been enabled!");
    }}

    @Override
    public void onDisable() {{
        getLogger().info("{plugin_name} has been disabled.");
    }}
}}
""")

    # Create plugin.yml
    with open("src/main/resources/plugin.yml", "w") as f:
        f.write(f"""name: {plugin_name}
version: 1.0
main: com.{author_dir}.{plugin_name.lower()}.Main
api-version: 1.16
author: {author_name}
""")

    # Optional default configs
    for filename in ["config.yml", "messages.yml"]:
        with open(f"src/main/resources/{filename}", "w") as f:
            f.write("# Default " + filename)
