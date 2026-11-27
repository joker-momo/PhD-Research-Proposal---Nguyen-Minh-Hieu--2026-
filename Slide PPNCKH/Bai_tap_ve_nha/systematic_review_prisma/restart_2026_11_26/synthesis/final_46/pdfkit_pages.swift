import Foundation
import PDFKit

guard CommandLine.arguments.count == 2,
      let document = PDFDocument(url: URL(fileURLWithPath: CommandLine.arguments[1])) else {
    fputs("Usage: swift pdfkit_pages.swift <local PDF>\n", stderr)
    exit(1)
}

let pages = (0..<document.pageCount).map { document.page(at: $0)?.string ?? "" }
FileHandle.standardOutput.write(try JSONEncoder().encode(pages))
