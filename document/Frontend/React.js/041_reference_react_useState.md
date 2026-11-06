# useState – React Official Documentation

`useState` is a React Hook that lets you add a state variable to your component.

```javascript
const [state, setState] = useState(initialState);
```

## Reference

### `useState(initialState)`

Call `useState` at the top level of your component to declare a state variable.

```javascript
import { useState } from 'react';

function MyComponent() {
  const [age, setAge] = useState(28);
  const [name, setName] = useState('Taylor');
  const [todos, setTodos] = useState(() => createInitialTodos());
  // ...
```

The convention is to name state variables like `[something, setSomething]` using array destructuring.

#### Parameters

- `initialState`: The value you want the state to be initially. It can be a value of any type, but there is a special behavior for functions. This argument is ignored after the initial render.
  - If you pass a function as `initialState`, it will be treated as an *initializer function*. It should be pure, should take no arguments, and should return a value of any type. React will call your initializer function when initializing the component, and store its return value.

#### Returns

`useState` returns an array with exactly two values:

1. The current state. During the first render, it will match the `initialState` you have passed.
2. The `set` function that lets you update the state to a different value and trigger a re-render.

#### Caveats

- `useState` is a Hook, so you can only call it **at the top level of your component** or your own Hooks. You cannot call it inside loops, conditions, or nested functions. If you need that, extract a new component and move the state into it.
- In Strict Mode, React will **call your updater and initializer functions twice** in development to help you find accidental impurities. This is dev-only behavior and does not affect production.

---

### `set` functions (`setSomething(nextState)`)

The `set` function returned by `useState` lets you update the state to a different value and trigger a re-render. You can pass the next state directly, or a function that calculates it from the previous state:

```javascript
const [name, setName] = useState('Edward');

function handleClick() {
  setName('Taylor');
  setAge(a => a + 1);
  // ...
```

#### Parameters

- `nextState`: The value that you want the state to be. It can be a value of any type, but there is a special behavior for functions.
  - If you pass a function as `nextState`, it will be treated as an *updater function*. It must be pure, should take the pending state as its only argument, and should return the next state. React will put your updater function in a queue and re-render your component. During the next render, React will calculate the next state by applying all of the queued updaters to the previous state.

#### Returns

`set` functions do not have a return value (they return `undefined`).

#### Caveats

- The `set` function **only updates the state variable for the *next* render**. If you read the state variable after calling the `set` function, you will still get the old value that was on the screen before your call.
- If the new value you provide is identical to the current `state`, as determined by an `Object.is` comparison, React will **skip re-rendering the component and its children**. This is an optimization.
- React **batches state updates**. It updates the screen after all the event handlers have run and have called their `set` functions. This prevents multiple re-renders during a single event.

---

## Usage Examples

### Adding state to a component

Call `useState` at the top level of your component to declare one or more state variables.

```javascript
import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <button onClick={handleClick}>
      You pressed me {count} times
    </button>
  );
}
```

### Updating state based on the previous state

Suppose the `age` is `42`. This handler calls `setAge(age + 1)` three times:

```javascript
function handleClick() {
  setAge(age + 1); // setAge(42 + 1)
  setAge(age + 1); // setAge(42 + 1)
  setAge(age + 1); // setAge(42 + 1)
}
```

However, after one click, `age` will only be `43`, not `45`! This is because calling the `set` function does not update the `age` state variable in the already running code.

To solve this problem, you can pass an **updater function** to `setAge` instead of the next state:

```javascript
function handleClick() {
  setAge(a => a + 1); // setAge(42 => 43)
  setAge(a => a + 1); // setAge(43 => 44)
  setAge(a => a + 1); // setAge(44 => 45)
}
```

Here, `a => a + 1` is your updater function. It takes the pending state and calculates the next state from it.

