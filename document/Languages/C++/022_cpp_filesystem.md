---
id: "c++_022"
technology: "C++"
category: "Languages"
title: "Filesystem library (since C++17) - cppreference.com"
doc_order: 22
source_url: "https://en.cppreference.com/cpp/filesystem"
language: "en"
retrieved_at: "2026-11-03 17:56:19"
content_hash: "c361e90c20d4bde8b34437333738f2fd14598e3e9f3c636d35bf1742ac3a9e70"
---

# Filesystem library (since C++17) - cppreference.com

Source: https://en.cppreference.com/cpp/filesystem

---

# Filesystem library (since C++17)

The Filesystem library provides facilities for performing operations on file systems and their components, such as paths, regular files, and directories.

The filesystem library was originally developed as [boost.filesystem](https://www.boost.org/doc/libs/release/libs/filesystem/doc/index.htm), was published as [the technical specification ISO/IEC TS 18822:2015](https://en.cppreference.com/cpp/experimental/fs), and finally merged to ISO C++ as of C++17. The boost implementation is currently available on more compilers and platforms than the C++17 library.

The filesystem library facilities may be unavailable if a hierarchical file system is not accessible to the implementation, or if it does not provide the necessary capabilities. Some features may not be available if they are not supported by the underlying file system (e.g. the FAT filesystem lacks symbolic links and forbids multiple hardlinks). In those cases, errors must be reported.

The behavior is [undefined](https://en.cppreference.com/cpp/language/ub) if the calls to functions in this library introduce a *file system race*, that is, when multiple threads, processes, or computers interleave access and modification to the same object in a file system.

#### Library-wide definitions

- *file*: a file system object that holds data, can be written to, read from, or both. Files have names, attributes, one of which is file type:

  - *directory*: a file that acts as a container of directory entries, which identify other files (some of which may be other, nested directories). When discussing a particular file, the directory in which it appears as an entry is its *parent directory*. The parent directory can be represented by the relative pathname `".."`.
  - *regular file*: a directory entry that associates a name with an existing file (i.e. a *hard link*). If multiple hard links are supported, the file is removed after the last hard link to it is removed.
  - *symbolic link*: a directory entry that associates a name with a path, which may or may not exist.
  - other special file types: *block*, *character*, *fifo*, *socket*.

- *file name*: a string of characters that names a file. Permissible characters, case sensitivity, maximum length, and the disallowed names are implementation-defined. Names `"."` (dot) and `".."` (dot-dot) have special meaning at library level.
- *path*: sequence of elements that identifies a file. It begins with an optional root-name (e.g. `"C:"` or `"//server"` on Windows), followed by an optional root-directory (e.g. `"/"` on Unix), followed by a sequence of zero or more file names (all but last of which have to be directories or links to directories). The native format (e.g. which characters are used as separators) and character encoding of the string representation of a path (the *pathname*) is implementation-defined, this library provides portable representation of paths.

  - *absolute path*: a path that unambiguously identifies the location of a file.
  - *canonical path*: an absolute path that includes no symlinks, `"."` or `".."` elements.
  - *relative path*: a path that identifies the location of a file relative to some location on the file system. The special path names `"."` (dot, "current directory") and `".."` (dot-dot, "parent directory") are relative paths.

| Classes |  | 
| Defined in  namespace `std::filesystem` |  | 
|  | represents a path (class) | 
|  | an exception thrown on file system errors (class) | 
|  | a directory entry (class) | 
|  | an iterator to the contents of the directory (class) | 
|  | an iterator to the contents of a directory and its subdirectories (class) | 
|  | represents file type and permissions (class) | 
|  | information about free and available space on the filesystem (class) | 
|  | the type of a file (enum) | 
|  | identifies file system permissions (enum) | 
|  | specifies semantics of permissions operations (enum) | 
|  | specifies semantics of copy operations (enum) | 
|  | options for iterating directory contents (enum) | 
|  | represents file time values (typedef) | 
| Non-member functions |  | 
| Defined in  namespace `std::filesystem` |  | 
|  | composes an absolute path (function) | 
|  | composes a canonical path (function) | 
|  | composes a relative path (function) | 
|  | copies files or directories (function) | 
|  | copies file contents (function) | 
|  | copies a symbolic link (function) | 
|  | creates new directory (function) | 
|  | creates a hard link (function) | 
|  | creates a symbolic link (function) | 
|  | returns or sets the current working directory (function) | 
|  | checks whether path refers to existing file system object (function) | 
|  | checks whether two paths refer to the same file system object (function) | 
|  | returns the size of a file (function) | 
|  | returns the number of hard links referring to the specific file (function) | 
|  | gets or sets the time of the last data modification (function) | 
|  | modifies file access permissions (function) | 
|  | obtains the target of a symbolic link (function) | 
|  | removes a file or empty directory removes a file or directory and all its contents, recursively (function) | 
|  | moves or renames a file or directory (function) | 
|  | changes the size of a regular file by truncation or zero-fill (function) | 
|  | determines available free space on the file system (function) | 
|  | determines file attributes determines file attributes, checking the symlink target (function) | 
|  | returns a directory suitable for temporary files (function) | 
| File types |  | 
|  | checks whether the given path refers to block device (function) | 
|  | checks whether the given path refers to a character device (function) | 
|  | checks whether the given path refers to a directory (function) | 
|  | checks whether the given path refers to an empty file or directory (function) | 
|  | checks whether the given path refers to a named pipe (function) | 
|  | checks whether the argument refers to an *other* file (function) | 
|  | checks whether the argument refers to a regular file (function) | 
|  | checks whether the argument refers to a named IPC socket (function) | 
|  | checks whether the argument refers to a symbolic link (function) | 
|  | checks whether file status is known (function) | 

### Notes

Using this library may require additional compiler/linker options. GNU implementation prior to 9.1 requires linking with `-lstdc++fs` and LLVM implementation prior to LLVM 9.0 requires linking with `-lc++fs`.

| [Feature-test](https://en.cppreference.com/cpp/utility/feature_test) macro | Value | Std | Feature | 
|---|---|---|---|
| [`__cpp_lib_filesystem`](https://en.cppreference.com/cpp/feature_test#cpp_lib_filesystem) | [`201703L`](https://en.cppreference.com/cpp/compiler_support/17#cpp_lib_filesystem_201703L) | (C++17) | Filesystem library |