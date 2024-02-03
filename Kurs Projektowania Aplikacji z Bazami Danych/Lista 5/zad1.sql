drop procedure if exists SaveTranExample;  
go 

create procedure SaveTranExample  
    @InputCustomerID int  
as   
    declare @TranCounter int = @@TRANCOUNT;
    print(@TranCounter)
    if @TranCounter > 0  
        save transaction ProcedureSave;  
    else   
        begin transaction;
    
    begin try  
        delete SalesLT.Customer  
            where CustomerID = @InputCustomerID;  
        if @TranCounter = 0  
            commit transaction;  
    end try  
    begin catch
        if @TranCounter = 0  
            rollback transaction;  
        else    
            if xact_state() <> -1  
                rollback transaction ProcedureSave;  
        print (error_message());  
    end catch  
go

begin transaction;
    exec SaveTranExample @InputCustomerID = 1;
commit transaction;
go


select * from SalesLT.Customer;
go
