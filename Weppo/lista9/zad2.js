const sql = require("mssql");
const config = require("./secret");

async function fetchData() {
  try {
    await sql.connect(config);
    const result = await sql.query("SELECT * FROM OSOBA");
    console.log(result.recordset);
  } catch (error) {
    console.error(error);
  } finally {
    await sql.close();
  }
}

async function insertData(name, surname, gender) {
  try {
    await sql.connect(config);
    const result =
      await sql.query`INSERT INTO OSOBA (IMIE, NAZWISKO, PLEC) OUTPUT INSERTED.ID VALUES (${name}, ${surname}, ${gender})`;
    console.log("Inserted record with ID:", result.recordset[0].ID);
  } catch (error) {
    console.error(error);
  } finally {
    await sql.close();
  }
}

async function updateData(id, newName) {
  try {
    await sql.connect(config);
    const result =
      await sql.query`UPDATE OSOBA SET IMIE = ${newName} WHERE ID = ${id}`;
    console.log("Updated", result.rowsAffected[0], "record(s)");
  } catch (error) {
    console.error(error);
  } finally {
    await sql.close();
  }
}

async function deleteData(id) {
  try {
    await sql.connect(config);
    const result = await sql.query`DELETE FROM OSOBA WHERE ID = ${id}`;
    console.log("Deleted", result.rowsAffected[0], "record(s)");
  } catch (error) {
    console.error(error);
  } finally {
    await sql.close();
  }
}

fetchData();
insertData("John", "Doe", "M");
updateData(1, "Jane");
deleteData(1);
