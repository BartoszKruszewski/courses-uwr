#### $while (b)\{...\} $

```
S: if b == 0 goto E
   ...
   goto S
E:
```

#### $for (i = 0; i < n; i++) \{...\}$

```
   i := 0
S: if i >= n goto E
   ...
   i := i + 1
   goto S
E:
```

#### $do\{...\}while (b) $

```
S: ...
   if b goto S
```
