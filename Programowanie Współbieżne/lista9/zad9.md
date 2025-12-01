#### Algorytm TAS

```java
public class TASLock implements Lock {
	AtomicBoolean state = new AtomicBoolean(false);
	public void lock() {
		while (state.getAndSet(true)) {}
	}
	public void unlock() {
		state.set(false);
	}
}
```

#### `isLocked()` TAS

```java
boolean isLocked() {
	return state.get();
}
```

#### Algorytm CLH

```java
public class CLHLock implements Lock {
	AtomicReference<QNode> tail = new AtomicReference<QNode>(new QNode());
	ThreadLocal<QNode> myPred;
	ThreadLocal<QNode> myNode;
	public CLHLock() {
		tail = new AtomicReference<QNode>(new QNode());
		myNode = new ThreadLocal<QNode>() {
			protected QNode initialValue() {
				return new QNode();
			}
		};
		myPred = new ThreadLocal<QNode>() {
			protected QNode initialValue() {
				return null;
			}
		};
	}
	public void lock() {
		QNode qnode = myNode.get();
		qnode.locked = true;
		QNode pred = tail.getAndSet(qnode);
		myPred.set(pred);
		while (pred.locked) {}
	}
	public void unlock() {
		QNode qnode = myNode.get();
		qnode.locked = false;
		myNode.set(myPred.get());
	}
}
```

#### `isLocked()` CLH

```java
boolean isLocked() {
	return tail.get().locked;
}
```

#### Algorytm MCS

```java
public class MCSLock implements Lock {
	AtomicReference<QNode> tail;
	ThreadLocal<QNode> myNode;
	public MCSLock() {
		queue = new AtomicReference<QNode>(null);
		myNode = new ThreadLocal<QNode>() {
			protected QNode initialValue() {
				return new QNode();
			}
		};
	}
	class QNode {
		boolean locked = false;
		QNode next = null;
	}
	public void lock() {
		QNode qnode = myNode.get();
		QNode pred = tail.getAndSet(qnode);
		if (pred != null) {
			qnode.locked = true;
			pred.next = qnode;
			// wait until predecessor gives up the lock
			while (qnode.locked) {}
		}
	}
	public void unlock() {
		QNode qnode = myNode.get();
		if (qnode.next == null) {
			if (tail.compareAndSet(qnode, null))
				return;
			// wait until predecessor fills in its next field
			while (qnode.next == null) {}
		}
		qnode.next.locked = false;
		qnode.next = null;
	}
}
```

#### `isLocked()` MCS

```java
boolean isLocked() {
	return tail.get() != null;
}
```