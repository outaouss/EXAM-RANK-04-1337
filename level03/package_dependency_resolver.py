def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    result = []
    visited = set()
    visiting = set()

    def dfs(package):
        if package in visiting:
            raise ValueError("Circular dependency detected")

        if package in visited:
            return

        visiting.add(package)

        for dependency in packages.get(package, []):
            dfs(dependency)

        visiting.remove(package)
        visited.add(package)
        result.append(package)

    for package in packages:
        dfs(package)

    return result
