from core.snapshot import get_snapshot
from core.analyzer import analyze

snap = get_snapshot()
result = analyze(snap)

print(result)