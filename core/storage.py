import os
from datetime import datetime
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment

class Storage:
    def __init__(self, output_dir="output/reports"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.workbook = openpyxl.Workbook()
        self.summary_sheet = self.workbook.active
        self.summary_sheet.title = "Summary"
        self.requests_sheet = self.workbook.create_sheet("Network Requests")
        self._setup_headers()

    def _setup_headers(self):
        summary_headers = [
            "Website URL", "Page Title", "Total Requests",
            "Payment API URLs", "UPI IDs Found", "Gateways Found",
            "Screenshot Path", "Timestamp"
        ]

        request_headers = [
            "Website URL", "Request Type", "Method",
            "API Endpoint", "Gateways Detected",
            "UPI IDs Found", "Post Data", "Timestamp"
        ]

        self._write_headers(self.summary_sheet, summary_headers)
        self._write_headers(self.requests_sheet, request_headers)

    def _write_headers(self, sheet, headers):
        header_font = Font(bold=True, color="FFFFFF")
        header_fill = PatternFill(
            start_color="1F4E79",
            end_color="1F4E79",
            fill_type="solid"
        )
        header_alignment = Alignment(horizontal="center", vertical="center")

        for col_num, header in enumerate(headers, 1):
            cell = sheet.cell(row=1, column=col_num, value=header)
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = header_alignment
            sheet.column_dimensions[
                openpyxl.utils.get_column_letter(col_num)
            ].width = max(15, len(header) + 5)

    def save_summary(self, summary):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        payment_urls = list(set([
            entry.get("url", "")
            for entry in summary.get("network_findings", [])
            if entry.get("url")
        ]))

        row = [
            summary.get("url", ""),
            summary.get("page_title", ""),
            summary.get("total_payment_requests", 0),
            "\n".join(payment_urls),       
            ", ".join(summary.get("all_upi_ids", [])),
            ", ".join(summary.get("all_gateways", [])),
            summary.get("screenshot_path", ""),
            timestamp
        ]

        self.summary_sheet.append(row)
        self.summary_sheet.row_dimensions[self.summary_sheet.max_row].height = 80

        row_num = self.summary_sheet.max_row
        self.summary_sheet.cell(row=row_num, column=4).alignment = Alignment(
            wrap_text=True, vertical="top"
        )
        print(f"[Storage] Summary row saved for: {summary.get('url', '')}")

    def save_requests(self, summary):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        website_url = summary.get("url", "")

        for entry in summary.get("network_findings", []):
            row = [
                website_url,
                entry.get("source", "").upper(),
                entry.get("method", ""),
                entry.get("url", ""),
                ", ".join(entry.get("gateways_found", [])),
                ", ".join(entry.get("upi_ids_found", [])),
                entry.get("post_data", "") or "",
                timestamp
            ]
            self.requests_sheet.append(row)

        print(f"[Storage] {len(summary.get('network_findings', []))} request rows saved")
    
    def save(self, summary):
        self.save_summary(summary)
        self.save_requests(summary)
        self._write_file()

    def _write_file(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"investigation_{timestamp}.xlsx"
        filepath = os.path.join(self.output_dir, filename)
        self.workbook.save(filepath)
        print(f"[Storage] Excel report saved: {filepath}")
        return filepath