const sql = require("mssql");
const config = require("./secret");

async function insertData(name, surname, workplaceName) {
  try {
    await sql.connect(config);
    const {
      recordset: [{ ID }],
    } = await sql.query`
      INSERT INTO MIEJSCE_PRACY (NAZWA)
      OUTPUT INSERTED.ID VALUES (${workplaceName});
    `;

    console.log("New workplace added with ID:", ID);

    await sql.query`
      INSERT INTO OSOBA (IMIE, NAZWISKO, ID_MIEJSCE_PRACY)
      VALUES (${name}, ${surname}, ${ID});
    `;

    console.log("New person added successfully");
  } catch (error) {
    console.error(error);
  } finally {
    await sql.close();
  }
}

insertData("John", "Doe", "Company A");
