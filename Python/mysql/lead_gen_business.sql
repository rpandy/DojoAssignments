SELECT * FROM billing;

-- What query would you run to get the total revenue for March of 2012? 
SELECT clients.client_id, clients.first_name, clients.last_name, SUM(billing.amount), billing.charged_datetime FROM clients
LEFT JOIN billing
ON clients.client_id = billing.client_id
WHERE billing.charged_datetime >= 2012-03-01 AND billing.charged_datetime <= 2012-03-31
GROUP BY clients.client_id
