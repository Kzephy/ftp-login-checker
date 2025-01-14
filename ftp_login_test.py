import ftplib

def ftp_login_test(ip_address, log_file):
    try:
        ftp = ftplib.FTP(ip_address, timeout=10)  # Timeout set to avoid hanging
        ftp.login('anonymous', '')
        log_file.write(f"Success! {ip_address} allows anonymous login\n")
        ftp.quit()
        return True
    
    except ftplib.all_errors as e:
        log_file.write(f"FTP Error! {ip_address} does not allow anonymous login.\n")
        return False
    
    except OSError as e:
        log_file.write(f"Socket Error! {ip_address} is unreachable.\n")
        return False

def ftp_srv_test(ip_list, log_file):
    for ip in ip_list:
        ftp_login_test(ip, log_file)

if __name__ == "__main__":
    # List your IP addresses here for testing
    ip_addresses = [
        "192.168.0.1",
        "ftp.gnu.org",
    ]
    
    # Export results to a text document
#    with open('ftp_login_test_output.txt', 'w') as log_file:
#        ftp_srv_test(ip_addresses, log_file)
