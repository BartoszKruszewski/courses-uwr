CARGO = cargo
TARGET = target/release/transport
BINARY = transport

all: build

build:
	rm -f $(BINARY)
	rm -rf target
	$(CARGO) build --release
	cp $(TARGET) $(BINARY)

run: build
	./$(BINARY)

clean:
	rm -rf target

distclean:
	rm -f $(BINARY)
	rm -rf target
