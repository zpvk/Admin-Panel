CREATE TABLE "Supplier" (
  "id" SERIAL PRIMARY KEY,
  "full_name" varchar,
  "contact_no" int,
  "email" varchar,
  "address" varchar,
  "city" varchar,
  "postal_code" int,
  "country" varchar,
  "available_raw_materials" varchar
);

CREATE TABLE "Customer" (
  "id" SERIAL PRIMARY KEY,
  "full_name" varchar,
  "address" varchar,
  "contact_no" int,
  "email" varchar,
  "city" varchar
);

CREATE TABLE "Employee" (
  "id" SERIAL PRIMARY KEY,
  "em_department_id" int,
  "manager_id" int,
  "full_name" varchar,
  "NIC" varchar,
  "gender" varchar,
  "email" varchar,
  "contact_no" int,
  "job_title" varchar,
  "hire_date" date,
  "date_of_birth" date,
  "age" int
);

CREATE TABLE "Dependent" (
  "id" SERIAL PRIMARY KEY,
  "full_name" varchar,
  "employee_id" int,
  "gender" varchar,
  "date_of_birth" date,
  "relationship" varchar
);

CREATE TABLE "Order" (
  "id" SERIAL PRIMARY KEY,
  "customer_id" int,
  "quantity" int,
  "order_decription_id" int,
  "order_recied_date" date,
  "hand_over_date" date
);

CREATE TABLE "Order_Description" (
  "id" SERIAL PRIMARY KEY,
  "quantity" int,
  "Order_Description_id" int,
  "catergory_id" varchar,
  "color" varchar,
  "size" varchar
);

CREATE TABLE "Raw_materials" (
  "id" SERIAL PRIMARY KEY,
  "supplier_id" int,
  "catergory" varchar,
  "available_quanity" int,
  "purchased_date" date
);

CREATE TABLE "Machine" (
  "id" SERIAL PRIMARY KEY,
  "machine_code" int,
  "catergory" varchar,
  "efficinecy" varchar,
  "waste_per_day" varchar,
  "purchased_date" date,
  "warranty_period" int
);

CREATE TABLE "Repair_history" (
  "id" SERIAL PRIMARY KEY,
  "isse_identified_date" date,
  "issue" varchar,
  "fixed_date" date,
  "machine_id" int,
  "machanic_name" varchar,
  "contact_no" int,
  "items_purchased" varchar,
  "spare_parts_cost" decimal,
  "charge" decimal
);

CREATE TABLE "Product" (
  "id" SERIAL PRIMARY KEY,
  "order_id" int,
  "catergory_id" int,
  "quantity" int,
  "manufature_date" date,
  "unit_in_stock" decimal,
  "unit_in_order" int
);

CREATE TABLE "Category" (
  "id" SERIAL PRIMARY KEY,
  "category_name" varchar,
  "size" varchar,
  "unit_price" decimal,
  "discount" int,
  "raw_material_category" varchar
);

CREATE TABLE "Waste" (
  "id" SERIAL PRIMARY KEY,
  "catergory" varchar,
  "quantity" int,
  "status" varchar
);

CREATE TABLE "Department" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "location" varchar,
  "employee_count" int
);

CREATE TABLE "Vehicale" (
  "id" SERIAL PRIMARY KEY,
  "plate_no" varchar,
  "service_date" date,
  "liscence_iisue_date" date
);

CREATE TABLE "Warehouse" (
  "id" SERIAL PRIMARY KEY,
  "location" varchar,
  "capacity" int,
  "stock" id
);

CREATE TABLE "Invoice" (
  "id" SERIAL PRIMARY KEY,
  "supplier_id" int,
  "issued_date" date,
  "unit_price" decimal,
  "quantity" int,
  "currency" varchar,
  "account_no" int,
  "total_price" decimal
);

CREATE TABLE "Salary" (
  "id" SERIAL PRIMARY KEY,
  "full_name" varchar,
  "job_title" varchar,
  "em_department_id" int,
  "basic_salary" decimal,
  "OT_salary_per_hour" decimal,
  "work_hours" timestamp,
  "deductions" decimal,
  "pay_date" date,
  "bank_name" varchar,
  "name_in_account" varchar,
  "branch" varchar,
  "account_no" int
);

CREATE TABLE "Sales" (
  "id" SERIAL PRIMARY KEY,
  "order_id" int,
  "paid_amount" decimal,
  "products_purchased" varchar,
  "quantity" int,
  "sales_date_time" datetime,
  "employee_id" int,
  "customer_id" int,
  "discount" decimal,
  "pay_method" varchar
);

CREATE TABLE "Customer_bill" (
  "id" SERIAL PRIMARY KEY,
  "order_id" int,
  "product_id" int,
  "unit_price" decimal,
  "quantity" int,
  "cost_per_catergory" decimal,
  "total_price" decimal,
  "discount" decimal
);

CREATE TABLE "Money_status" (
  "id" SERIAL PRIMARY KEY,
  "sale_id" int,
  "customer_id" int,
  "supplier_id" int,
  "paid_amount" decimal,
  "paid_date" date
);

ALTER TABLE "Employee" ADD FOREIGN KEY ("em_department_id") REFERENCES "Department" ("id");

ALTER TABLE "Dependent" ADD FOREIGN KEY ("employee_id") REFERENCES "Employee" ("id");

ALTER TABLE "Order" ADD FOREIGN KEY ("customer_id") REFERENCES "Customer" ("id");

ALTER TABLE "Order" ADD FOREIGN KEY ("order_decription_id") REFERENCES "Order_Description" ("id");

ALTER TABLE "Order_Description" ADD FOREIGN KEY ("Order_Description_id") REFERENCES "Order" ("id");

ALTER TABLE "Category" ADD FOREIGN KEY ("id") REFERENCES "Order_Description" ("catergory_id");

ALTER TABLE "Supplier" ADD FOREIGN KEY ("id") REFERENCES "Raw_materials" ("supplier_id");

ALTER TABLE "Machine" ADD FOREIGN KEY ("id") REFERENCES "Repair_history" ("machine_id");

ALTER TABLE "Product" ADD FOREIGN KEY ("order_id") REFERENCES "Order" ("id");

ALTER TABLE "Product" ADD FOREIGN KEY ("catergory_id") REFERENCES "Category" ("id");

ALTER TABLE "Raw_materials" ADD FOREIGN KEY ("catergory") REFERENCES "Category" ("raw_material_category");

ALTER TABLE "Invoice" ADD FOREIGN KEY ("supplier_id") REFERENCES "Supplier" ("id");

ALTER TABLE "Invoice" ADD FOREIGN KEY ("unit_price") REFERENCES "Category" ("unit_price");

ALTER TABLE "Invoice" ADD FOREIGN KEY ("quantity") REFERENCES "Order" ("quantity");

ALTER TABLE "Salary" ADD FOREIGN KEY ("full_name") REFERENCES "Employee" ("full_name");

ALTER TABLE "Salary" ADD FOREIGN KEY ("job_title") REFERENCES "Employee" ("job_title");

ALTER TABLE "Salary" ADD FOREIGN KEY ("em_department_id") REFERENCES "Department" ("id");
