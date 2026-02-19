class Closer:
    @staticmethod
    def close(resource) -> None:
        """Close a resource if it has a close method."""
        if resource and hasattr(resource, "close") and callable(resource.close):
            try:
                resource.close()
            except Exception:
                pass  # Ignore errors during close