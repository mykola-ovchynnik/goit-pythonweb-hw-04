import asyncio
import argparse
import logging
from aiopath import AsyncPath
import aioshutil

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def parse_arguments():
    parser = argparse.ArgumentParser(description="Sort files into subfolders based on their extensions.")
    parser.add_argument("source", type=str, help="Path to the source folder.")
    parser.add_argument("output", type=str, help="Path to the output folder.")
    return parser.parse_args()


async def copy_file(file_path: AsyncPath, output_folder: AsyncPath):
    try:
        extension = file_path.suffix[1:] if file_path.suffix else "unknown"
        target_folder = output_folder / extension
        await target_folder.mkdir(parents=True, exist_ok=True)

        destination = target_folder / file_path.name
        await aioshutil.copyfile(file_path, destination)
        logging.info(f"Copied: {file_path} -> {destination}")
    except Exception as e:
        logging.error(f"Error copying {file_path}: {e}")


async def read_folder(source_folder: AsyncPath, output_folder: AsyncPath):
    tasks = []
    async for file_path in source_folder.rglob("*"):
        if await file_path.is_file():
            tasks.append(copy_file(file_path, output_folder))

    await asyncio.gather(*tasks)
    logging.info("Sorting completed.")


async def main():
    args = parse_arguments()
    source_folder = AsyncPath(args.source)
    output_folder = AsyncPath(args.output)

    if not await source_folder.exists() or not await source_folder.is_dir():
        logging.error("Source folder does not exist or is not a directory.")
        return

    await output_folder.mkdir(parents=True, exist_ok=True)
    await read_folder(source_folder, output_folder)


if __name__ == "__main__":
    asyncio.run(main())
