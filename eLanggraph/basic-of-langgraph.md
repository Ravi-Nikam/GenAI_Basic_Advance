# LangGraph Syntax Cheat Sheet

| Syntax | Easy Meaning |
|--------|-------------|
| `TypedDict` | Tells what is inside the dictionary |
| `State` | Stores graph data |
| `Annotated` | Adds extra information |
| `add_messages` | Handles message updates |
| `def chatbot()` | Function that does the work |
| `add_node()` | Adds a node |
| `START` | Graph starts here |
| `END` | Graph ends here |
| `add_edge()` | Joins nodes |
| `compile()` | Prepares graph |
| `invoke()` | Runs graph |
| `HumanMessage()` | User's message |

## One Line to Remember

> State → Node → Edge → START → Node → END → Invoke

## More Accurately
State defines data
↓
Node does work
↓
Edge connects nodes
↓
START begins
↓
END finishes
↓
invoke() runs everything