import express from 'express';
import fs from 'fs';
import path from 'path';

const app = express();

app.get('/list-files', (req, res) => {
	const directoryPath = path.join(__dirname, 'D:/KMUTNB-CS/OOPject/comfile/foldercopy');

	fs.readdir(directoryPath, { withFileTypes: true }, async (err, files) => {
		if (err) {
			return res.status(500).send('Unable to scan files!');
		}

		const fileList = await Promise.all(
			files.map(async (file) => {
				const filePath = path.join(directoryPath, file.name);
				const isDir = file.isDirectory();
				return {
					name: file.name,
					type: isDir ? 'folder' : 'file',
					...(isDir && { contents: await fetchDirectoryContents(filePath) })
				};
			})
		);
		res.json(fileList);
	});
});

async function fetchDirectoryContents(dir) {
	const files = await fs.promises.readdir(dir, { withFileTypes: true });
	return Promise.all(
		files.map(async (file) => {
			return {
				name: file.name,
				type: file.isDirectory() ? 'folder' : 'file'
			};
		})
	);
}
