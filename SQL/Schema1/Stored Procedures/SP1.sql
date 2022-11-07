CREATE OR REPLACE PROCEDURE Schema4.SP1()
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
