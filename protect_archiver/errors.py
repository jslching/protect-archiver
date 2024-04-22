class Errors:
    def __init__(self) -> None:
        pass

    @Exception
    class ProtectError(Exception):
        def __init__(self, code: int) -> None:
            self.code = code

    class DownloadFailed(Exception):
        def __init__(self, message: str) -> None:
            super().__init__(message)

    class AuthorizationFailed(Exception):
        def __init__(self, message: str) -> None:
            super().__init__(message)
