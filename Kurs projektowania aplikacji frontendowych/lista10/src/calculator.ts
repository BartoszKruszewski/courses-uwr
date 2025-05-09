import { evaluate } from 'mathjs'

export class Calculator {
    private expression = ''

    public get display(): string {
        return this.expression || '0'
    }

    public append(char: string) {
        this.expression += char
    }

    public pop() {
        this.expression = this.expression.slice(0, -1)
    }

    public clear() {
        this.expression = ''
    }

    public compute(): string {
        try {
            const result = evaluate(this.expression)
            this.expression = String(result)
            return this.expression
        } catch {
            this.expression = ''
            return 'Error'
        }
    }
}
