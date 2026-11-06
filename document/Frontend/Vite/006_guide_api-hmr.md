---
id: "vite_006"
technology: "Vite"
category: "Frontend"
title: "HMR API | Vite"
doc_order: 6
source_url: "https://vite.dev/guide/api-hmr"
language: "en"
retrieved_at: "2026-11-03 17:58:56"
content_hash: "15bd7a219da20c83d6ffce645deeb82ca42c3e7d136773d57b4ef0e6d1f06995"
---

# HMR API | Vite

Source: https://vite.dev/guide/api-hmr

---

# HMR API [](https://vite.dev#hmr-api)

Note

This is the client HMR API. For handling HMR update in plugins, see [handleHotUpdate](https://vite.dev/api-plugin#handlehotupdate).

The manual HMR API is primarily intended for framework and tooling authors. As an end user, HMR is likely already handled for you in the framework specific starter templates.

Vite exposes its manual HMR API via the special `import.meta.hot` object:

```
interface ImportMeta {
  readonly hot?: ViteHotContext
}
interface ViteHotContext {
  readonly data: any
  accept(): void
  accept(cb: (mod: ModuleNamespace | undefined) => void): void
  accept(dep: string, cb: (mod: ModuleNamespace | undefined) => void): void
  accept(
    deps: readonly string[],
    cb: (mods: Array<ModuleNamespace | undefined>) => void,
  ): void
  dispose(cb: (data: any) => void): void
  prune(cb: (data: any) => void): void
  invalidate(message?: string): void
  on<T extends CustomEventName>(
    event: T,
    cb: (payload: InferCustomEventPayload<T>) => void,
  ): void
  off<T extends CustomEventName>(
    event: T,
    cb: (payload: InferCustomEventPayload<T>) => void,
  ): void
  send<T extends CustomEventName>(
    event: T,
    data?: InferCustomEventPayload<T>,
  ): void
}
```
## Required Conditional Guard [](https://vite.dev#required-conditional-guard)

First of all, make sure to guard all HMR API usage with a conditional block so that the code can be tree-shaken in production:

```
if (import.meta.hot) {
  // HMR code
}
```
## IntelliSense for TypeScript [](https://vite.dev#intellisense-for-typescript)

Vite provides type definitions for `import.meta.hot` in [`vite/client.d.ts`](https://github.com/vitejs/vite/blob/main/packages/vite/client.d.ts). You can add "vite/client" in the `tsconfig.json` so TypeScript picks up the type definitions:

```
{
  "compilerOptions": {
    "types": ["vite/client"]
  }
}
```
## `hot.accept(cb)` [](https://vite.dev#hot-accept-cb)

For a module to self-accept, use `import.meta.hot.accept` with a callback which receives the updated module:

```
export const count = 1
if (import.meta.hot) {
  import.meta.hot.accept((newModule) => {
    if (newModule) {
      // newModule is undefined when SyntaxError happened
      console.log('updated: count is now ', newModule.count)
    }
  })
}
```
A module that "accepts" hot updates is considered an **HMR boundary**.

Vite's HMR does not actually swap the originally imported module: if an HMR boundary module re-exports imports from a dep, then it is responsible for updating those re-exports (and these exports must be using `let`). In addition, importers up the chain from the boundary module will not be notified of the change. This simplified HMR implementation is sufficient for most dev use cases, while allowing us to skip the expensive work of generating proxy modules.

Vite requires that the call to this function appears as `import.meta.hot.accept(` (whitespace-sensitive) in the source code in order for the module to accept update. This is a requirement of the static analysis that Vite does to enable HMR support for a module.

## `hot.accept(deps, cb)` [](https://vite.dev#hot-accept-deps-cb)

A module can also accept updates from direct dependencies without reloading itself:

```
import { foo } from './foo.js'
foo()
if (import.meta.hot) {
  import.meta.hot.accept('./foo.js', (newFoo) => {
    // the callback receives the updated './foo.js' module
    newFoo?.foo()
  })
  // Can also accept an array of dep modules:
  import.meta.hot.accept(
    ['./foo.js', './bar.js'],
    ([newFooModule, newBarModule]) => {
      // The callback receives an array where only the updated module is
      // non null. If the update was not successful (syntax error for ex.),
      // the array is empty
    },
  )
}
```
## `hot.dispose(cb)` [](https://vite.dev#hot-dispose-cb)

A self-accepting module or a module that expects to be accepted by others can use `hot.dispose` to clean-up any persistent side effects created by its updated copy:

```
function setupSideEffect() {}
setupSideEffect()
if (import.meta.hot) {
  import.meta.hot.dispose((data) => {
    // cleanup side effect
  })
}
```
## `hot.prune(cb)` [](https://vite.dev#hot-prune-cb)

Register a callback that will be called when the module is no longer imported on the page. Compared to `hot.dispose`, this can be used if the source code cleans up side-effects by itself on updates and you only need to clean-up when it's removed from the page. Vite currently uses this for `.css` imports.

```
function setupOrReuseSideEffect() {}
setupOrReuseSideEffect()
if (import.meta.hot) {
  import.meta.hot.prune((data) => {
    // cleanup side effect
  })
}
```
## `hot.data` [](https://vite.dev#hot-data)

Vite creates one `import.meta.hot.data` object for each module path. The object is persisted across successive instances of the same module during HMR. Mutations made during module execution or through the `data` argument passed to `hot.dispose` are visible to the next instance of the module.

When a module is pruned, its `hot.dispose` and `hot.prune` callbacks receive the current data object. Vite clears the data after those callbacks complete. If the module is imported again later, it receives a new empty data object.

Note that re-assignment of `data` itself is not supported. Instead, you should mutate properties of the `data` object so information added from other handlers are preserved.

```
// ok
import.meta.hot.data.someValue = 'hello'
// not supported
import.meta.hot.data = { someValue: 'hello' }
```
## `hot.decline()` [](https://vite.dev#hot-decline)

This is currently a noop and is there for backward compatibility. This could change in the future if there is a new usage for it. To indicate that the module is not hot-updatable, use `hot.invalidate()`.

## `hot.invalidate(message?: string)` [](https://vite.dev#hot-invalidate-message-string)

A self-accepting module may realize during runtime that it can't handle a HMR update, and so the update needs to be forcefully propagated to importers. By calling `import.meta.hot.invalidate()`, the HMR server will invalidate the importers of the caller, as if the caller wasn't self-accepting. This will log a message both in the browser console and in the terminal. You can pass a message to give some context on why the invalidation happened.

Note that you should always call `import.meta.hot.accept` even if you plan to call `invalidate` immediately afterwards, or else the HMR client won't listen for future changes to the self-accepting module. To communicate your intent clearly, we recommend calling `invalidate` within the `accept` callback like so:

```
import.meta.hot.accept((module) => {
  // You may use the new module instance to decide whether to invalidate.
  if (cannotHandleUpdate(module)) {
    import.meta.hot.invalidate()
  }
})
```
## `hot.on(event, cb)` [](https://vite.dev#hot-on-event-cb)

Listen to an HMR event.

The following HMR events are dispatched by Vite automatically:

- `'vite:beforeUpdate'` when an update is about to be applied (e.g. a module will be replaced)
- `'vite:afterUpdate'` when an update has just been applied (e.g. a module has been replaced)
- `'vite:beforeFullReload'` when a full reload is about to occur
- `'vite:beforePrune'` when modules that are no longer needed are about to be pruned
- `'vite:invalidate'` when a module is invalidated with `import.meta.hot.invalidate()`
- `'vite:error'` when an error occurs (e.g. syntax error)
- `'vite:ws:disconnect'` when the WebSocket connection is lost
- `'vite:ws:connect'` when the WebSocket connection is (re-)established

Custom HMR events can also be sent from plugins. See [handleHotUpdate](https://vite.dev/api-plugin#handlehotupdate) for more details.

## `hot.off(event, cb)` [](https://vite.dev#hot-off-event-cb)

Remove callback from the event listeners.

## `hot.send(event, data)` [](https://vite.dev#hot-send-event-data)

Send custom events back to Vite's dev server.

If called before connected, the data will be buffered and sent once the connection is established.

See [Client-server Communication](https://vite.dev/guide/api-plugin#client-server-communication) for more details, including a section on [Typing Custom Events](https://vite.dev/guide/api-plugin#typescript-for-custom-events).

## Further Reading [](https://vite.dev#further-reading)

If you'd like to learn more about how to use the HMR API and how it works under-the-hood. Check out these resources: