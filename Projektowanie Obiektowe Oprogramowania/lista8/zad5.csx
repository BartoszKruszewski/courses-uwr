using System;

var machine = new CoffeeMachine();

machine.Handle("select");        // Waiting for coin.
machine.Handle("insert_coin");   // Coin inserted.
machine.Handle("select");        // Making coffee...
machine.Handle("select");        // Waiting for coin.

abstract class State
{
    protected CoffeeMachine Machine;

    public State(CoffeeMachine machine)
    {
        Machine = machine;
    }

    public abstract void Handle(string action);
}

class IdleState : State
{
    public IdleState(CoffeeMachine machine) : base(machine) {}

    public override void Handle(string action)
    {
        if (action == "insert_coin")
        {
            Console.WriteLine("Coin inserted.");
            Machine.SetState(Machine.ReadyState);
        }
        else
        {
            Console.WriteLine("Waiting for coin.");
        }
    }
}

class ReadyState : State
{
    public ReadyState(CoffeeMachine machine) : base(machine) {}

    public override void Handle(string action)
    {
        if (action == "select")
        {
            Console.WriteLine("Making coffee...");
            Machine.SetState(Machine.IdleState);
        }
        else
        {
            Console.WriteLine("Please select coffee.");
        }
    }
}

class CoffeeMachine
{
    public State IdleState { get; }
    public State ReadyState { get; }

    private State _state;

    public CoffeeMachine()
    {
        IdleState = new IdleState(this);
        ReadyState = new ReadyState(this);
        _state = IdleState;
    }

    public void SetState(State state)
    {
        _state = state;
    }

    public void Handle(string action)
    {
        _state.Handle(action);
    }
}
