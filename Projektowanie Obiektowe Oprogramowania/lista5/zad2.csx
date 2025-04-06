using System;
using System.IO;

public class CaesarStream : Stream
{
    Stream s;
    int shift;

    public CaesarStream(Stream s, int shift)
    {
        this.s = s;
        this.shift = shift;
    }

    public override bool CanRead => s.CanRead;
    public override bool CanSeek => s.CanSeek;
    public override bool CanWrite => s.CanWrite;
    public override long Length => s.Length;
    public override long Position { get => s.Position; set => s.Position = value; }
    public override void Flush() => s.Flush();
    public override long Seek(long offset, SeekOrigin origin) => s.Seek(offset, origin);
    public override void SetLength(long value) => s.SetLength(value);

    public override void Write(byte[] buffer, int offset, int count)
    {
        for (int i = 0; i < count; i++)
            buffer[offset + i] = (byte)(buffer[offset + i] + shift);
        s.Write(buffer, offset, count);
    }

    public override int Read(byte[] buffer, int offset, int count)
    {
        int read = s.Read(buffer, offset, count);
        for (int i = 0; i < read; i++)
            buffer[offset + i] = (byte)(buffer[offset + i] + shift);
        return read;
    }
}

var data = new byte[] { 10, 20, 30, 40, 50 };

using (var file = File.Create("test.bin"))
using (var cae = new CaesarStream(file, 5))
    cae.Write(data, 0, data.Length);

var result = new byte[5];
using (var file = File.OpenRead("test.bin"))
using (var cae = new CaesarStream(file, -5))
    cae.Read(result, 0, result.Length);

Console.WriteLine(string.Join(", ", result));
