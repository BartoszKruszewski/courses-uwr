import os
import signal
import socket
import subprocess
import time
from pathlib import Path

import psutil


SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = "9000"
DATA_SIZE = "9000000"

CWD = Path(__file__).parent
REFERENCE_PROGRAM = CWD / "transport-client-fast"
MY_PROGRAM = CWD / "transport"
OUTPUT_REFERENCE = CWD / "output_reference"
OUTPUT_MYPROGRAM = CWD / "output_myprogram"

DUMMY_DATA = b"GARBAGE1234567890"
WAIT_BEFORE_STOP = 1
WAIT_AFTER_SEND = 1


def run_benchmark(program_path: Path, output_file: Path):
    print(f"Running {program_path.name}...")
    start = time.time()

    proc = subprocess.Popen(
        [str(program_path), SERVER_ADDRESS, SERVER_PORT, output_file.name, DATA_SIZE],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    ps_proc = psutil.Process(proc.pid)
    max_ram = 0

    try:
        while proc.poll() is None:
            ram = ps_proc.memory_info().rss

            for child in ps_proc.children(recursive=True):
                try:
                    ram += child.memory_info().rss
                except psutil.NoSuchProcess:
                    continue

            ram_kb = ram // 1024  # KB
            if ram_kb > max_ram:
                max_ram = ram_kb

            time.sleep(0.05)  # 50 ms
    except psutil.NoSuchProcess:
        pass

    end = time.time()

    elapsed_ms = (end - start) * 1000  # ms
    
    print(f"Real time: {elapsed_ms:.2f} ms")
    print(f"Max memory: {max_ram} KB\n")

    return elapsed_ms, max_ram


def find_source_port_udp(pid):
    """Znajdź port źródłowy UDP dla danego PID."""
    try:
        proc = psutil.Process(pid)
        for conn in proc.connections(kind='udp'):
            if conn.laddr:
                return conn.laddr.port
    except psutil.NoSuchProcess:
        return None
    return None


def send_garbage_udp(port):
    """Wyślij śmieci na wskazany port UDP."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.sendto(DUMMY_DATA, (SERVER_ADDRESS, port))
            print(f"Sent UDP garbage to port {port}")
        except Exception as e:
            print(f"Failed to send UDP garbage: {e}")


def is_same_files() -> bool:
    if not OUTPUT_REFERENCE.exists() or not OUTPUT_MYPROGRAM.exists():
        return False
    if OUTPUT_REFERENCE.read_bytes() == OUTPUT_MYPROGRAM.read_bytes():
        return True
    return False


def run_garbage_injection_test():
    print(f"Running {MY_PROGRAM.name} with UDP garbage injection...")

    proc = subprocess.Popen(
        [str(MY_PROGRAM), SERVER_ADDRESS, SERVER_PORT, OUTPUT_MYPROGRAM.name, DATA_SIZE],
        cwd=CWD,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(WAIT_BEFORE_STOP)

    print("Stopping process...")
    os.kill(proc.pid, signal.SIGSTOP)

    port = find_source_port_udp(proc.pid)
    if port is None:
        print("\033[31mFAILED: Could not find UDP port.\033[0m")
        proc.kill()
        return

    print(f"Found source UDP port: {port}")

    send_garbage_udp(port)

    time.sleep(WAIT_AFTER_SEND)

    print("Resuming process...")
    os.kill(proc.pid, signal.SIGCONT)

    proc.wait()

    print("Process finished.")


if __name__ == "__main__":
    OUTPUT_REFERENCE.unlink(missing_ok=True)
    OUTPUT_MYPROGRAM.unlink(missing_ok=True)

    ref_time, ref_mem = run_benchmark(REFERENCE_PROGRAM, OUTPUT_REFERENCE)
    my_time, my_mem = run_benchmark(MY_PROGRAM, OUTPUT_MYPROGRAM)
    same_files = is_same_files()

    OUTPUT_MYPROGRAM.unlink(missing_ok=True)

    run_garbage_injection_test()
    injection_proof = is_same_files()

    GOOD = "\033[32mOK\033[0m"
    BAD = "\033[31mFAILED\033[0m"

    print()
    print("Same files: " + (GOOD if same_files else BAD))
    print("Time: " + (GOOD if my_time <= 4 * ref_time + 5000 else BAD))
    print("Memory: " + (GOOD if my_mem <= 6000 else BAD))
    print("Injection-proof: " + (GOOD if injection_proof else BAD))
