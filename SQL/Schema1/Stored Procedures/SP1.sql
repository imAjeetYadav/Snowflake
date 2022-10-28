CREATE OR REPLACE PROCEDURE Schema1.simple_stored_procedure_example()
returns string not null
language javascript
as
$$
var cmd = `
<SOME SUPER SWEET SQL STATEMENT>
`
var sql = snowflake.createStatement({sqlText: cmd});
var result = sql.execute();
return '💰';
$$;
