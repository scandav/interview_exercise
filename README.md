1. Create a `Location` table in the database in order to save location details (name and address of hospital/doctor). See `models.py`
2. Apply modifications to the database schema.
3. Load data contained in `fixtures`
4. Create a view for `/measurements` accepting a GET request with query params: patient name (partial match is valid) and eye (left or right - 1 or 2) and returning a JSON file containing `result`, `date`, `measurement_done`
5. show results for `/measurements/?patient=John&eye=2`, `/measurements/?patient=John&eye=2`, `/measurements/?patient=Paul&eye=2`
