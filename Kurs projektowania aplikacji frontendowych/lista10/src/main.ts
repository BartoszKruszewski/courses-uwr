import { Calculator } from './calculator'

const calc = new Calculator()
const displayEl = document.getElementById('display') as HTMLDivElement

function render() {
    displayEl.textContent = calc.display
}

document.querySelectorAll<HTMLButtonElement>('.calc__key').forEach(btn => {
    const key = btn.dataset.key
    if (!key) return

    btn.addEventListener('click', () => {
        calc.append(key)
        render()
    })
})

document.getElementById('clear')?.addEventListener('click', () => {
    calc.clear()
    render()
})

document.getElementById('del')?.addEventListener('click', () => {
    calc.pop()
    render()
})

document.getElementById('eq')?.addEventListener('click', () => {
    displayEl.textContent = calc.compute()
})

render()