"""Minimal example for BridgeWatch."""

from bridgewatch import bridgewatch


def main():
 runner = bridgewatch({"name": "BridgeWatch", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()