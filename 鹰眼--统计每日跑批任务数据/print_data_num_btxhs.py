import pymysql

import time
import xlrd
import xlwt
from ku import c,h
from xlutils.copy import copy
t_time=time.strftime('%Y-%m-%d',time.localtime())

t_name='跑批任务报告-王朋朝.xlsx'
read=xlrd.open_workbook(t_name,formatting_info=True)
wb=copy(read)
sheet2=wb.get_sheet(t_time)

db = pymysql.connect("xxx", "root", "xx", h)
cur=db.cursor()
sql="""
SELECT
 -- a.company_name AS '客户名称',
count(*) as count
 -- b.character_name AS '统计标签名称',
 -- a.result_data AS '结果',
 -- a.character_code,
-- DATE_FORMAT( a.date_time, "%Y-%m-%d" ) 
FROM
 tb_data_runbatch a
 LEFT JOIN tb_character_info b ON a.character_code = b.character_code 
WHERE
  a.result_data NOT LIKE "%null%" 
 and a.result_data NOT LIKE '%: 0%' 
 AND a.result_data NOT LIKE '[]' 
 AND a.result_data NOT LIKE '[{}]' 
 AND a.result_data IS NOT NULL 
 AND
DATE_FORMAT( date_time, "%Y-%m-%d" )=DATE_FORMAT(NOW(),'%Y-%m-%d' )  and
 a.character_type='2'
 AND a.character_code IN (
 SELECT DISTINCT
  a.character_code 
 FROM
  tb_character_info a
  LEFT JOIN tb_character_type b ON a.character_type_id = b.id 
 WHERE
  a.character_type = '2' 
  AND a.character_status = '1' 
  AND a.audit_status = '1' 
--   AND b.show_name LIKE '%涉税风险%' 
  AND b.show_name LIKE '%法海预警信号%' 
) 
"""
cur.execute(sql)
res=cur.fetchone()[0]
print('统计标签：',res)
sheet2.write(8,7,res)

sql="""
SELECT
--  a.company_name AS '客户名称',
--  b.character_name AS '统计标签名称',
--  a.result_data AS '结果',
--  a.character_code 
count(*) as count
FROM
 tb_data_runbatch a
 LEFT JOIN tb_character_info b ON a.character_code = b.character_code 
WHERE
  result_data LIKE '%RST%' 
  AND DATE_FORMAT( date_time, "%Y-%m-%d" )=DATE_FORMAT(NOW(),'%Y-%m-%d' ) 
and a.character_type='3'
 and a.character_code IN (
 SELECT DISTINCT
  character_code 
 FROM
  tb_re_rule_info 
 WHERE
  rule_code IN (
  SELECT DISTINCT
   a.rule_code 
  FROM
   tb_re_rule_info a
   LEFT JOIN tb_character_type b ON a.result_type = b.id 
  WHERE
   b.show_name LIKE '%法海预警信号%' 
   AND del_flag = '0' 
   AND rule_status = '1' 
   AND check_status = '1' 
  ) 
  AND check_status = '1' 
  AND del_flag = '0' 
  AND rule_status = '1' 
 )  
"""
cur.execute(sql)
res=cur.fetchone()[0]
print('规则结果：',res)
sheet2.write(8,8,res)

sql="""
select count(*) from tb_character_data_rel where date_time=DATE_FORMAT(NOW(),'%Y-%m-%d' )
and character_code in 
(SELECT DISTINCT
  a.character_code 
 FROM
  tb_character_info a
  LEFT JOIN tb_character_type b ON a.character_type_id = b.id 
 WHERE
  a.character_type = '2' 
  AND a.character_status = '1' 
  AND a.audit_status = '1' 
  AND b.show_name LIKE '法海预警信号%'

 ) and date_time=DATE_FORMAT(NOW(),'%Y-%m-%d' ) ORDER BY company_name
"""
cur.execute(sql)
res=cur.fetchone()[0]
print('溯源：',res)
sheet2.write(8,15,res)

sql="""
SELECT
count(*)
	-- customer_name AS '企业名称',
	-- signal_rating AS '风险等级',
	-- signal_event AS '风险事件',
  -- create_time	
FROM
	`tb_warn_signal` 
	WHERE 
-- signal_generation_stage = '3' and-- 贷后
	DATE_FORMAT( create_time, "%Y-%m-%d" ) = DATE_FORMAT(NOW(),'%Y-%m-%d' ) 
and is_manual=0 and id_number in 
(select id_number from tb_manager_customer_personal where is_delete=0 union 
select id_number from tb_relation_customer where customer_type='P')
"""
cur.execute(sql)
res=cur.fetchone()[0]
print('个人信号：',res)
sheet2.write(9,9,res)

sql="""
SELECT
count(*)
-- 	customer_name AS '企业名称',
-- 	signal_rating AS '风险等级',
-- 	signal_event AS '风险事件',
--   create_time	
FROM
	`tb_warn_signal` 
	WHERE 
	-- signal_generation_stage = '3' and-- 贷后
	DATE_FORMAT( create_time, "%Y-%m-%d" ) = DATE_FORMAT(NOW(),'%Y-%m-%d' ) 
and is_manual=0 and customer_name in 
(select  customer_name from tb_manage_customer where is_delete=0 union 
select customer_relation_name from tb_relation_customer where customer_type='C')
"""
cur.execute(sql)
res=cur.fetchone()[0]
print('企业贷后信号：',res)
sheet2.write(9,10,res)

sql="""
select count(*) from tb_factors_list_json where factors_type='1' and is_real='0'  and SUBSTRING_index(company_name,'_',-1) 
in (select id_number from tb_manager_customer_personal where is_delete=0 union 
select id_number from tb_relation_customer where customer_type='P')and 
( DATE_FORMAT(last_update_time,'%Y-%m-%d')=DATE_FORMAT(NOW(),'%Y-%m-%d') or
 DATE_FORMAT(create_time,'%Y-%m-%d')=DATE_FORMAT(NOW(),'%Y-%m-%d') );
"""
cur.execute(sql)
res=cur.fetchone()[0]
print('存量个人画像：',res)
sheet2.write(10,11,res)

sql="""
select count(*) from tb_factors_list_json where factors_type='1' and is_real='0'  and company_name 
in (select DISTINCT customer_name from tb_manage_customer where is_delete=0 union 
select customer_relation_name from tb_relation_customer where customer_type='C')and 
( DATE_FORMAT(last_update_time,'%Y-%m-%d')=DATE_FORMAT(NOW(),'%Y-%m-%d') or
 DATE_FORMAT(create_time,'%Y-%m-%d')=DATE_FORMAT(NOW(),'%Y-%m-%d') );
"""
cur.execute(sql)
res=cur.fetchone()[0]
print('企业画像：',res)
sheet2.write(10,12,res)

sql="""
select count(*) from tb_factors_list_json where factors_type='2' and is_real='0'  and SUBSTRING_index(company_name,'_',-1) 
in (select id_number from tb_manager_customer_personal where is_delete=0 union 
select id_number from tb_relation_customer where customer_type='P')and 
( DATE_FORMAT(last_update_time,'%Y-%m-%d')=DATE_FORMAT(NOW(),'%Y-%m-%d') or
 DATE_FORMAT(create_time,'%Y-%m-%d')=DATE_FORMAT(NOW(),'%Y-%m-%d') );
"""
cur.execute(sql)
res=cur.fetchone()[0]
print('个人报告：',res)
sheet2.write(10,13,res)

sql="""
select count(*) from tb_factors_list_json where factors_type='2' and is_real='0'  and company_name 
in (select DISTINCT customer_name from tb_manage_customer where is_delete=0 union 
select customer_relation_name from tb_relation_customer where customer_type='C')and 
( DATE_FORMAT(last_update_time,'%Y-%m-%d')=DATE_FORMAT(NOW(),'%Y-%m-%d') or
 DATE_FORMAT(create_time,'%Y-%m-%d')=DATE_FORMAT(NOW(),'%Y-%m-%d') )
"""
cur.execute(sql)
res=cur.fetchone()[0]
print('企业报告：',res)
sheet2.write(10,14,res)

wb.save(t_name)