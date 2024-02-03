import { Person } from "./zad5_a";
import { persons } from "./zad5_a";

function logPerson(person: Person) {
  let additionalInformation: string = "";

  if (person.role) additionalInformation = person.role;
  else if (person.occupation) additionalInformation = person.occupation;
  console.log(`- ${person.name}, ${person.age}, ${additionalInformation}`);
}
