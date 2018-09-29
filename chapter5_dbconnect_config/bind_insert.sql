set echo on

--@@db_config.sql
--connect &user/&pw@&connect_string

begin
  execute immediate 'drop table mytab';
exception
when others then
  if sqlcode not in (-00942) then
    raise;
  end if;
end;
/

create table mytab (id number, data varchar2(20), constraint my_pk primary key (id));

-- select * from mytab;
-- truncate table mytab;

commit ;